import unittest

from ge_validator import datasource


class BuildTrinoConnectionStringTests(unittest.TestCase):
    """Regression tests for the malformed-URL bug:
    a --host carrying a scheme/port produced trino://user@https://host:8080:8080/...,
    which SQLAlchemy parsed to an empty port -> ValueError: invalid literal for int().
    """

    def test_plain_host_and_port(self):
        url = datasource.build_trino_connection_string(
            "presto-gateway.example.net", 8080, "alice", "etl", "public_test1"
        )
        self.assertEqual(url, "trino://alice@presto-gateway.example.net:8080/etl/public_test1")

    def test_scheme_in_host_is_stripped(self):
        url = datasource.build_trino_connection_string(
            "https://presto-gateway.example.net:8080", 8080, "alice", "etl", "public_test1"
        )
        # no 'https://' embedded, no doubled ':8080:8080'
        self.assertEqual(url, "trino://alice@presto-gateway.example.net:8080/etl/public_test1")
        self.assertNotIn("https://", url)
        self.assertNotIn(":8080:8080", url)

    def test_embedded_port_in_host_wins_over_port_arg(self):
        url = datasource.build_trino_connection_string(
            "presto-gateway.example.net:9090", 8080, "alice", "etl", "public_test1"
        )
        self.assertEqual(url, "trino://alice@presto-gateway.example.net:9090/etl/public_test1")

    def test_produces_a_single_valid_port(self):
        # the exact shape that used to blow up
        url = datasource.build_trino_connection_string(
            "https://presto-gateway.presto.stg.aws.fwmrm.net:8080", 8080, "kd", "etl", "public_test1"
        )
        # everything after the last ':' up to the next '/' must be an int
        host_port = url.split("@", 1)[1].split("/", 1)[0]
        port_str = host_port.rsplit(":", 1)[1]
        self.assertEqual(int(port_str), 8080)  # would raise ValueError under the old bug


class BuildEngineKwargsTests(unittest.TestCase):
    def test_connect_args_carry_https_scheme(self):
        kwargs = datasource.build_engine_kwargs(
            {"host": "https://gw:8080", "port": 8080, "user": "alice",
             "catalog": "etl", "schema": "public_test1", "http_headers": {"Authorization": "Bearer x"}}
        )
        self.assertIn("connect_args", kwargs)
        self.assertEqual(kwargs["connect_args"].get("http_scheme"), "https")

    def test_connect_args_include_authenticated_session(self):
        kwargs = datasource.build_engine_kwargs(
            {"host": "gw", "port": 8080, "user": "alice", "catalog": "etl",
             "schema": "public_test1", "http_headers": {"Authorization": "Bearer tok123"}}
        )
        session = kwargs["connect_args"].get("http_session")
        self.assertIsNotNone(session)
        self.assertEqual(session.headers.get("Authorization"), "Bearer tok123")


if __name__ == "__main__":
    unittest.main()
