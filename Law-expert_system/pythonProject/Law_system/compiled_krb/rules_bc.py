# rules_bc.py

from pyke import contexts, pattern, bc_rule

pyke_version = '1.1.1'
compiler_version = 1

def no_money(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_it_divorce_case', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.no_money: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_M_have_incubation', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.no_money: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def inc(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_it_divorce_case', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.inc: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_M_have_incubation', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.inc: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def kids(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_it_divorce_case', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.kids: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_M_have_incubation', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.kids: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def brea(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_it_divorce_case', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.brea: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_M_have_incubation', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.brea: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_child_under_2years', context,
                                  (rule.pattern(0),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "rules.brea: got unexpected plan from when clause 3"
                    rule.rule_base.num_bc_rule_successes += 1
                    yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def house(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_it_divorce_case', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.house: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_M_have_incubation', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.house: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_wife_staying_your_house', context,
                                  (rule.pattern(1),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "rules.house: got unexpected plan from when clause 3"
                    rule.rule_base.num_bc_rule_successes += 1
                    yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def servant(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_it_divorce_case', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.servant: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_M_have_incubation', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.servant: got unexpected plan from when clause 2"
                with engine.prove('questions', 'is_D_rich', context,
                                  (rule.pattern(0),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "rules.servant: got unexpected plan from when clause 3"
                    rule.rule_base.num_bc_rule_successes += 1
                    yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def her_divorce(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_it_divorce_case', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.her_divorce: got unexpected plan from when clause 1"
            with engine.prove('questions', 'ch_div_st', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.her_divorce: got unexpected plan from when clause 2"
                if context.lookup_data('ans') in (2,):
                  rule.rule_base.num_bc_rule_successes += 1
                  yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def her_div(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_it_divorce_case', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.her_div: got unexpected plan from when clause 1"
            with engine.prove('questions', 'ch_div_st', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.her_div: got unexpected plan from when clause 2"
                if context.lookup_data('ans') in (2,):
                  rule.rule_base.num_bc_rule_successes += 1
                  yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def harm_expense(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_it_divorce_case', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.harm_expense: got unexpected plan from when clause 1"
            with engine.prove('questions', 'ch_div_st', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.harm_expense: got unexpected plan from when clause 2"
                if context.lookup_data('ans') in (3,):
                  with engine.prove('questions', 'any_defect', context,
                                    (rule.pattern(2),)) \
                    as gen_4:
                    for x_4 in gen_4:
                      assert x_4 is None, \
                        "rules.harm_expense: got unexpected plan from when clause 4"
                      rule.rule_base.num_bc_rule_successes += 1
                      yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def not_harm_expense(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_it_divorce_case', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.not_harm_expense: got unexpected plan from when clause 1"
            with engine.prove('questions', 'ch_div_st', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.not_harm_expense: got unexpected plan from when clause 2"
                if context.lookup_data('ans') in (1,):
                  with engine.prove('questions', 'any_defect', context,
                                    (rule.pattern(2),)) \
                    as gen_4:
                    for x_4 in gen_4:
                      assert x_4 is None, \
                        "rules.not_harm_expense: got unexpected plan from when clause 4"
                      rule.rule_base.num_bc_rule_successes += 1
                      yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def expense(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_it_divorce_case', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.expense: got unexpected plan from when clause 1"
            with engine.prove('questions', 'ch_div_st', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.expense: got unexpected plan from when clause 2"
                if context.lookup_data('ans') in (1,3):
                  with engine.prove('questions', 'any_defect', context,
                                    (rule.pattern(2),)) \
                    as gen_4:
                    for x_4 in gen_4:
                      assert x_4 is None, \
                        "rules.expense: got unexpected plan from when clause 4"
                      rule.rule_base.num_bc_rule_successes += 1
                      yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def after_divorce(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_it_divorce_case', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.after_divorce: got unexpected plan from when clause 1"
            with engine.prove('questions', 'ch_div_st', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.after_divorce: got unexpected plan from when clause 2"
                if context.lookup_data('ans') in (1,3):
                  with engine.prove('questions', 'is_it_in_contract', context,
                                    (rule.pattern(0),)) \
                    as gen_4:
                    for x_4 in gen_4:
                      assert x_4 is None, \
                        "rules.after_divorce: got unexpected plan from when clause 4"
                      with engine.prove('questions', 'any_defect', context,
                                        (rule.pattern(2),)) \
                        as gen_5:
                        for x_5 in gen_5:
                          assert x_5 is None, \
                            "rules.after_divorce: got unexpected plan from when clause 5"
                          rule.rule_base.num_bc_rule_successes += 1
                          yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def aft_divorce(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_it_divorce_case', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.aft_divorce: got unexpected plan from when clause 1"
            with engine.prove('questions', 'ch_div_st', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.aft_divorce: got unexpected plan from when clause 2"
                if context.lookup_data('ans') in (1,3):
                  with engine.prove('questions', 'is_it_in_contract', context,
                                    (rule.pattern(2),)) \
                    as gen_4:
                    for x_4 in gen_4:
                      assert x_4 is None, \
                        "rules.aft_divorce: got unexpected plan from when clause 4"
                      with engine.prove('questions', 'is_there_witness', context,
                                        (rule.pattern(0),)) \
                        as gen_5:
                        for x_5 in gen_5:
                          assert x_5 is None, \
                            "rules.aft_divorce: got unexpected plan from when clause 5"
                          with engine.prove('questions', 'any_defect', context,
                                            (rule.pattern(2),)) \
                            as gen_6:
                            for x_6 in gen_6:
                              assert x_6 is None, \
                                "rules.aft_divorce: got unexpected plan from when clause 6"
                              rule.rule_base.num_bc_rule_successes += 1
                              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def incubation(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_it_divorce_case', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.incubation: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_ch_und_15', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.incubation: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def m_incubation(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_it_divorce_case', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.m_incubation: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_ch_und_15', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.m_incubation: got unexpected plan from when clause 2"
                with engine.prove('questions', 'any_def_m', context,
                                  (rule.pattern(0),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "rules.m_incubation: got unexpected plan from when clause 3"
                    rule.rule_base.num_bc_rule_successes += 1
                    yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def f_incubation(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_it_divorce_case', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.f_incubation: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_ch_und_15', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.f_incubation: got unexpected plan from when clause 2"
                with engine.prove('questions', 'any_def_m', context,
                                  (rule.pattern(1),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "rules.f_incubation: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'any_def_f', context,
                                      (rule.pattern(0),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "rules.f_incubation: got unexpected plan from when clause 4"
                        rule.rule_base.num_bc_rule_successes += 1
                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def mm_incubation(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_it_divorce_case', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.mm_incubation: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_ch_und_15', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.mm_incubation: got unexpected plan from when clause 2"
                with engine.prove('questions', 'any_def_m', context,
                                  (rule.pattern(1),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "rules.mm_incubation: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'any_def_f', context,
                                      (rule.pattern(1),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "rules.mm_incubation: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'any_def_mm', context,
                                          (rule.pattern(0),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "rules.mm_incubation: got unexpected plan from when clause 5"
                            rule.rule_base.num_bc_rule_successes += 1
                            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def fm_incubation(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_it_divorce_case', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.fm_incubation: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_ch_und_15', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.fm_incubation: got unexpected plan from when clause 2"
                with engine.prove('questions', 'any_def_m', context,
                                  (rule.pattern(1),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "rules.fm_incubation: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'any_def_f', context,
                                      (rule.pattern(1),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "rules.fm_incubation: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'any_def_mm', context,
                                          (rule.pattern(1),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "rules.fm_incubation: got unexpected plan from when clause 5"
                            with engine.prove('questions', 'any_def_fm', context,
                                              (rule.pattern(0),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "rules.fm_incubation: got unexpected plan from when clause 6"
                                rule.rule_base.num_bc_rule_successes += 1
                                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def ms_incubation(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_it_divorce_case', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.ms_incubation: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_ch_und_15', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.ms_incubation: got unexpected plan from when clause 2"
                with engine.prove('questions', 'any_def_m', context,
                                  (rule.pattern(1),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "rules.ms_incubation: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'any_def_f', context,
                                      (rule.pattern(1),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "rules.ms_incubation: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'any_def_mm', context,
                                          (rule.pattern(1),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "rules.ms_incubation: got unexpected plan from when clause 5"
                            with engine.prove('questions', 'any_def_fm', context,
                                              (rule.pattern(1),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "rules.ms_incubation: got unexpected plan from when clause 6"
                                with engine.prove('questions', 'any_def_ms', context,
                                                  (rule.pattern(0),)) \
                                  as gen_7:
                                  for x_7 in gen_7:
                                    assert x_7 is None, \
                                      "rules.ms_incubation: got unexpected plan from when clause 7"
                                    rule.rule_base.num_bc_rule_successes += 1
                                    yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def fs_incubation(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_it_divorce_case', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.fs_incubation: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_ch_und_15', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.fs_incubation: got unexpected plan from when clause 2"
                with engine.prove('questions', 'any_def_m', context,
                                  (rule.pattern(1),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "rules.fs_incubation: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'any_def_f', context,
                                      (rule.pattern(1),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "rules.fs_incubation: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'any_def_mm', context,
                                          (rule.pattern(1),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "rules.fs_incubation: got unexpected plan from when clause 5"
                            with engine.prove('questions', 'any_def_fm', context,
                                              (rule.pattern(1),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "rules.fs_incubation: got unexpected plan from when clause 6"
                                with engine.prove('questions', 'any_def_ms', context,
                                                  (rule.pattern(1),)) \
                                  as gen_7:
                                  for x_7 in gen_7:
                                    assert x_7 is None, \
                                      "rules.fs_incubation: got unexpected plan from when clause 7"
                                    with engine.prove('questions', 'any_def_fs', context,
                                                      (rule.pattern(0),)) \
                                      as gen_8:
                                      for x_8 in gen_8:
                                        assert x_8 is None, \
                                          "rules.fs_incubation: got unexpected plan from when clause 8"
                                        rule.rule_base.num_bc_rule_successes += 1
                                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def no_incubation(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions', 'is_it_divorce_case', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules.no_incubation: got unexpected plan from when clause 1"
            with engine.prove('questions', 'is_ch_und_15', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "rules.no_incubation: got unexpected plan from when clause 2"
                with engine.prove('questions', 'any_def_m', context,
                                  (rule.pattern(1),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "rules.no_incubation: got unexpected plan from when clause 3"
                    with engine.prove('questions', 'any_def_f', context,
                                      (rule.pattern(1),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "rules.no_incubation: got unexpected plan from when clause 4"
                        with engine.prove('questions', 'any_def_mm', context,
                                          (rule.pattern(1),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "rules.no_incubation: got unexpected plan from when clause 5"
                            with engine.prove('questions', 'any_def_fm', context,
                                              (rule.pattern(1),)) \
                              as gen_6:
                              for x_6 in gen_6:
                                assert x_6 is None, \
                                  "rules.no_incubation: got unexpected plan from when clause 6"
                                with engine.prove('questions', 'any_def_ms', context,
                                                  (rule.pattern(1),)) \
                                  as gen_7:
                                  for x_7 in gen_7:
                                    assert x_7 is None, \
                                      "rules.no_incubation: got unexpected plan from when clause 7"
                                    with engine.prove('questions', 'any_def_fs', context,
                                                      (rule.pattern(1),)) \
                                      as gen_8:
                                      for x_8 in gen_8:
                                        assert x_8 is None, \
                                          "rules.no_incubation: got unexpected plan from when clause 8"
                                        rule.rule_base.num_bc_rule_successes += 1
                                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def populate(engine):
  This_rule_base = engine.get_create('rules')
  
  bc_rule.bc_rule('no_money', This_rule_base, 'what_to_happen',
                  no_money, None,
                  (pattern.pattern_literal('husband_will_not_pay_money_for_kids_incubation'),),
                  (),
                  (pattern.pattern_literal(True),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('inc', This_rule_base, 'what_to_happen',
                  inc, None,
                  (pattern.pattern_literal('husband_will_pay_money_for_kids_incubation'),),
                  (),
                  (pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('kids', This_rule_base, 'what_to_happen',
                  kids, None,
                  (pattern.pattern_literal('husband_will_pay_money_for_kids_to_live_a_suitable_life'),),
                  (),
                  (pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('brea', This_rule_base, 'what_to_happen',
                  brea, None,
                  (pattern.pattern_literal('husband_will_pay_for_breastfeeding'),),
                  (),
                  (pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('house', This_rule_base, 'what_to_happen',
                  house, None,
                  (pattern.pattern_literal('husband_will_pay_rent_for_kids_house'),),
                  (),
                  (pattern.pattern_literal(True),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('servant', This_rule_base, 'what_to_happen',
                  servant, None,
                  (pattern.pattern_literal('husband_will_pay_for_a_servant'),),
                  (),
                  (pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('her_divorce', This_rule_base, 'what_to_happen',
                  her_divorce, None,
                  (pattern.pattern_literal('the_wife_will_give_up_on_all_her_rights'),),
                  (),
                  (pattern.pattern_literal(True),
                   contexts.variable('ans'),))
  
  bc_rule.bc_rule('her_div', This_rule_base, 'what_to_happen',
                  her_div, None,
                  (pattern.pattern_literal('the_wife_will_give_husband_money_before_marriage_back'),),
                  (),
                  (pattern.pattern_literal(True),
                   contexts.variable('ans'),))
  
  bc_rule.bc_rule('harm_expense', This_rule_base, 'what_to_happen',
                  harm_expense, None,
                  (pattern.pattern_literal('husband_pay_expense_from_2to5_years_of_the_monthly_aliment'),),
                  (),
                  (pattern.pattern_literal(True),
                   contexts.variable('ans'),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('not_harm_expense', This_rule_base, 'what_to_happen',
                  not_harm_expense, None,
                  (pattern.pattern_literal('husband_pay_24_month_expense_of_the_monthly_aliment'),),
                  (),
                  (pattern.pattern_literal(True),
                   contexts.variable('ans'),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('expense', This_rule_base, 'what_to_happen',
                  expense, None,
                  (pattern.pattern_literal('husband_pay_3_month_expense_of_the_monthly_aliment'),),
                  (),
                  (pattern.pattern_literal(True),
                   contexts.variable('ans'),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('after_divorce', This_rule_base, 'what_to_happen',
                  after_divorce, None,
                  (pattern.pattern_literal('husband_pay_after_divorce_money'),),
                  (),
                  (pattern.pattern_literal(True),
                   contexts.variable('ans'),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('aft_divorce', This_rule_base, 'what_to_happen',
                  aft_divorce, None,
                  (pattern.pattern_literal('husband_pay_after_divorce_money'),),
                  (),
                  (pattern.pattern_literal(True),
                   contexts.variable('ans'),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('incubation', This_rule_base, 'what_to_happen',
                  incubation, None,
                  (pattern.pattern_literal('there_is_no_incubation_the_children_free_to_choose_who_to_live_with'),),
                  (),
                  (pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('m_incubation', This_rule_base, 'what_to_happen',
                  m_incubation, None,
                  (pattern.pattern_literal('the_mother_will_have_the_incubation'),),
                  (),
                  (pattern.pattern_literal(False),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('f_incubation', This_rule_base, 'what_to_happen',
                  f_incubation, None,
                  (pattern.pattern_literal('the_father_will_have_the_incubation'),),
                  (),
                  (pattern.pattern_literal(False),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('mm_incubation', This_rule_base, 'what_to_happen',
                  mm_incubation, None,
                  (pattern.pattern_literal('the_mothers_mother_will_have_the_incubation'),),
                  (),
                  (pattern.pattern_literal(False),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('fm_incubation', This_rule_base, 'what_to_happen',
                  fm_incubation, None,
                  (pattern.pattern_literal('the_fathers_mother_will_have_the_incubation'),),
                  (),
                  (pattern.pattern_literal(False),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('ms_incubation', This_rule_base, 'what_to_happen',
                  ms_incubation, None,
                  (pattern.pattern_literal('the_mothers_sister_will_have_the_incubation'),),
                  (),
                  (pattern.pattern_literal(False),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('fs_incubation', This_rule_base, 'what_to_happen',
                  fs_incubation, None,
                  (pattern.pattern_literal('the_fathers_sister_will_have_the_incubation'),),
                  (),
                  (pattern.pattern_literal(False),
                   pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('no_incubation', This_rule_base, 'what_to_happen',
                  no_incubation, None,
                  (pattern.pattern_literal('the_child_will_go_to_a_shelter'),),
                  (),
                  (pattern.pattern_literal(False),
                   pattern.pattern_literal(True),))


Krb_filename = '..\\rules.krb'
Krb_lineno_map = (
    ((14, 18), (2, 2)),
    ((20, 25), (4, 4)),
    ((26, 31), (5, 5)),
    ((44, 48), (8, 8)),
    ((50, 55), (10, 10)),
    ((56, 61), (11, 11)),
    ((74, 78), (14, 14)),
    ((80, 85), (16, 16)),
    ((86, 91), (17, 17)),
    ((104, 108), (20, 20)),
    ((110, 115), (22, 22)),
    ((116, 121), (23, 23)),
    ((122, 127), (24, 24)),
    ((140, 144), (27, 27)),
    ((146, 151), (29, 29)),
    ((152, 157), (30, 30)),
    ((158, 163), (31, 31)),
    ((176, 180), (34, 34)),
    ((182, 187), (36, 36)),
    ((188, 193), (37, 37)),
    ((194, 199), (38, 38)),
    ((212, 216), (41, 41)),
    ((218, 223), (43, 43)),
    ((224, 229), (44, 44)),
    ((230, 230), (45, 45)),
    ((243, 247), (48, 48)),
    ((249, 254), (50, 50)),
    ((255, 260), (51, 51)),
    ((261, 261), (52, 52)),
    ((274, 278), (55, 55)),
    ((280, 285), (57, 57)),
    ((286, 291), (58, 58)),
    ((292, 292), (59, 59)),
    ((293, 298), (60, 60)),
    ((311, 315), (63, 63)),
    ((317, 322), (65, 65)),
    ((323, 328), (66, 66)),
    ((329, 329), (67, 67)),
    ((330, 335), (68, 68)),
    ((348, 352), (71, 71)),
    ((354, 359), (73, 73)),
    ((360, 365), (74, 74)),
    ((366, 366), (75, 75)),
    ((367, 372), (76, 76)),
    ((385, 389), (79, 79)),
    ((391, 396), (81, 81)),
    ((397, 402), (82, 82)),
    ((403, 403), (83, 83)),
    ((404, 409), (84, 84)),
    ((410, 415), (85, 85)),
    ((428, 432), (88, 88)),
    ((434, 439), (90, 90)),
    ((440, 445), (91, 91)),
    ((446, 446), (92, 92)),
    ((447, 452), (93, 93)),
    ((453, 458), (94, 94)),
    ((459, 464), (95, 95)),
    ((477, 481), (98, 98)),
    ((483, 488), (100, 100)),
    ((489, 494), (101, 101)),
    ((507, 511), (104, 104)),
    ((513, 518), (106, 106)),
    ((519, 524), (107, 107)),
    ((525, 530), (108, 108)),
    ((543, 547), (111, 111)),
    ((549, 554), (113, 113)),
    ((555, 560), (114, 114)),
    ((561, 566), (115, 115)),
    ((567, 572), (116, 116)),
    ((585, 589), (119, 119)),
    ((591, 596), (121, 121)),
    ((597, 602), (122, 122)),
    ((603, 608), (123, 123)),
    ((609, 614), (124, 124)),
    ((615, 620), (125, 125)),
    ((633, 637), (129, 129)),
    ((639, 644), (131, 131)),
    ((645, 650), (132, 132)),
    ((651, 656), (133, 133)),
    ((657, 662), (134, 134)),
    ((663, 668), (135, 135)),
    ((669, 674), (136, 136)),
    ((687, 691), (139, 139)),
    ((693, 698), (141, 141)),
    ((699, 704), (142, 142)),
    ((705, 710), (143, 143)),
    ((711, 716), (144, 144)),
    ((717, 722), (145, 145)),
    ((723, 728), (146, 146)),
    ((729, 734), (147, 147)),
    ((747, 751), (150, 150)),
    ((753, 758), (152, 152)),
    ((759, 764), (153, 153)),
    ((765, 770), (154, 154)),
    ((771, 776), (155, 155)),
    ((777, 782), (156, 156)),
    ((783, 788), (157, 157)),
    ((789, 794), (158, 158)),
    ((795, 800), (159, 159)),
    ((813, 817), (162, 162)),
    ((819, 824), (164, 164)),
    ((825, 830), (165, 165)),
    ((831, 836), (166, 166)),
    ((837, 842), (167, 167)),
    ((843, 848), (168, 168)),
    ((849, 854), (169, 169)),
    ((855, 860), (170, 170)),
    ((861, 866), (171, 171)),
)
