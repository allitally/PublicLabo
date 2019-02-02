#
#
#
from lark import Lark
import sys
import os
from syntax import SimpleLang

######################
def print_usage():
    print('''
usage: parseCs <file>
''')
######################
if len(sys.argv)<2:
    print_usage()
    exit(1)
    
dirname = os.path.dirname(sys.argv[0])
if dirname==None or len(dirname)==0:
    dirname="."
rule = open(dirname+'/grammar.txt').read()
target=open(sys.argv[1]).read()
parser = Lark(rule,start = "program", parser = 'lalr')
tree = parser.parse(target)

if tree != None:
    # print (tree)
    env = SimpleLang.Environment(None)
    v = SimpleLang.Visitor()
    ans = v.program(tree,env)
    print ("OK.",ans)

