from src.concurrency.event_bus import PriorityEventBus

def test_event_bus_wildcard():
    bus = PriorityEventBus()
    events = []
    bus.subscribe("system.*", lambda p: events.append(f"sys:{p}"))
    bus.subscribe("system.alert", lambda p: events.append(f"alert:{p}"))
    bus.subscribe("network.*", lambda p: events.append(f"net:{p}"))

    bus.publish("system.alert", "HighLoad")
    assert "sys:HighLoad" in events
    assert "alert:HighLoad" in events
    assert not any("net:" in e for e in events)
