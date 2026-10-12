from src.cli.args import get_parser
def test_cli_parser():
    p = get_parser()
    args = p.parse_args(['up'])
    assert args.cmd == 'up'
