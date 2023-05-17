import contextlib
import sys

from pyke import knowledge_engine
from pyke import krb_traceback

engine = knowledge_engine.engine(__file__)

def family_court():

    engine.reset()

    engine.activate('rules')
    
    try:
        with engine.prove_goal('rules.what_to_happen($event)') as rule:
            for vars, plan in rule:
                print("%s" % (vars['event']))
    except Exception:
        krb_traceback.print_exc()
        sys.exit(1)

    print()
    print("thanks for using our system")
family_court()

