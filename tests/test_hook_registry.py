from src.plugins.registry import HookRegistry

def test_hook_registry_priority():
    reg = HookRegistry()
    log = []
    reg.register("before_run", lambda: log.append("second"), priority=50)
    reg.register("before_run", lambda: log.append("first"), priority=10)
    reg.register("before_run", lambda: log.append("third"), priority=90)

    res = reg.emit("before_run")
    assert log == ["first", "second", "third"]
    assert len(res) == 3
