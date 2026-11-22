from src.observability.health_check import HealthChecker

def test_health_checker():
    hc = HealthChecker()
    hc.register_probe("disk_space", lambda: True)
    hc.register_probe("network_ping", lambda: False)

    res = hc.run_check()
    assert res["status"] == "UNHEALTHY"
    assert res["probes"]["disk_space"] == "PASS"
    assert res["probes"]["network_ping"] == "FAIL"
