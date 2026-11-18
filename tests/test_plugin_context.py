from src.plugins.context import PluginContext

def test_plugin_context_isolation():
    ctx = PluginContext("exec-001", {"timeout": 30})
    ctx.set_value("auth_token", "bearer-xyz")
    assert ctx.get_value("auth_token") == "bearer-xyz"
    assert ctx.is_cancelled is False
    ctx.cancel()
    assert ctx.is_cancelled is True
