import argparse
def get_parser():
    p = argparse.ArgumentParser(prog='sql-migrator')
    sub = p.add_subparsers(dest='cmd')
    sub.add_parser('up')
    sub.add_parser('down')
    sub.add_parser('status')
    return p
