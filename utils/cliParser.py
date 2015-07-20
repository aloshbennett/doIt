'''
Created on Jul 18, 2015

@author: msoundar
'''
import logging;

logger = logging.getLogger("doIt");

def parseInput(cli_terms, cmd_terms=["do","by","complete","show"]):
    
    logger.debug("input command - " + str(cli_terms));

    do_it = {};
    cmd = None;
    it = [];
    for term in cli_terms:
        if term in cmd_terms:
            do_it[cmd] = it; 
            cmd = term;
            it = [];
        else:
            it.append(term);
    do_it[cmd] = it;
    if None in do_it:
        del do_it[None];        
    logger.debug("parser output = " + str(do_it));
    
    return do_it;