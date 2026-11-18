from src.plugins.filter import InterceptorChain

def test_interceptor_chain():
    chain = InterceptorChain()
    chain.add_interceptor(lambda s: s.strip())
    chain.add_interceptor(lambda s: s.lower())
    chain.add_interceptor(lambda s: f"[{s}]")

    assert chain.process("  HELLO WORLD  ") == "[hello world]"
