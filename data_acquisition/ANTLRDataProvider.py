import pandas as pd

from antlr4 import *

from cpp_antlr.CPP14Lexer import CPP14Lexer
from cpp_antlr.CPP14Parser import CPP14Parser
from cpp_antlr.CPP14ParserListener import CPP14ParserListener


class CPP14FunctionListener(CPP14ParserListener):

    def __init__(self):
        self.functions = []

    def enterFunctionDefinition(self, ctx: CPP14Parser.FunctionDefinitionContext):
        size = ctx.stop.start - ctx.start.stop  # TODO look deeper what size I want
        content = str(ctx.start.source[1])[ctx.start.start:ctx.stop.stop + 1]
        class_name = ctx.children[
            0].stop.text  # Does this work always? #TODO search for token index or type? #TODO add namespaces
        function_name = str(ctx.children[1].start.source[1])[
                        ctx.children[1].start.start:ctx.children[1].stop.stop]  # TODO extract only function name!
        self.functions.append((class_name, function_name, content, size))

    def get_functions(self):
        return self.functions


def parse_file(filepath: str):
    input_stream = FileStream(filepath)
    lexer = CPP14Lexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CPP14Parser(stream)
    parser.buildParseTrees = True
    tree = parser.translationUnit()
    listener = CPP14FunctionListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    return listener.get_functions()


def parse_files(filenames: pd.Series):
    functions = []

    for filename in filenames:
        if str(filename).endswith((".h", ".cpp")):
            functions.extend(parse_file(filename))

    data = pd.DataFrame(functions, columns=["class", "function", "content", "size"])
    return data
