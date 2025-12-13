from lexer import Lexer
from parser import Parser
from codegen import CodeGen

file_name = "input.toy"
with open(file_name) as f:
    text_input = f.read()

lexer = Lexer().get_lexer()
tokens = lexer.lex(text_input)

# for token in tokens:
#     print(token)

codegen = CodeGen()

module = codegen.module
builder = codegen.builder
printf = codegen.printf

pg = Parser(module, builder, printf)
pg.parse()
parser = pg.get_parser()
parser.parse(tokens).eval()

codegen.create_ir()
codegen.save_ir("output.ll")
