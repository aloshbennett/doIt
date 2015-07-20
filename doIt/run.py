'''
Created on Jul 18, 2015

@author: msoundar
'''

import sys;
import logging;

import doIt;
from utils import cliParser;

logging.basicConfig(level=logging.DEBUG);
logger = logging.getLogger("doIt");

'''
    sample inputs
    1. do code review by 17/07
    2. do submission by 17/07
'''
    
if __name__ == "__main__":
    cmd_map = cliParser.parseInput(sys.argv[1:]);
    cmd_keywords = set(cmd_map.keys());
    if cmd_keywords.intersection(doIt.do_keywords):
        doIt.do(cmd_map);
    elif cmd_keywords.intersection(doIt.done_keywords):
        doIt.done(cmd_map);
    elif cmd_keywords.intersection(doIt.schedule_keywords):
        doIt.schedule(cmd_map);
    elif cmd_keywords.intersection(doIt.display_keywords):
        doIt.display();
        