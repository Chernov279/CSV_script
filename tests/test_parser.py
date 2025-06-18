from parser import Parser


def test_parser_args(monkeypatch):
    args = ['--file', 'test.csv', '--where', 'price>1000', '--aggregate', 'price=avg']
    monkeypatch.setattr('sys.argv', ['prog'] + args)
    parser = Parser().parse_args()
    assert parser.file == 'test.csv'
    assert parser.where == 'price>1000'
    assert parser.aggregate == 'price=avg'
