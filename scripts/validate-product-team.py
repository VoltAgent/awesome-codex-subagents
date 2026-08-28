#!/usr/bin/env python3
from __future__ import annotations
import sys, tomllib
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
TEAM = ROOT / "teams" / "product-engineering"
errors=[]
for p in [TEAM/'AGENTS.md', TEAM/'config.toml', TEAM/'agents', TEAM/'contracts', TEAM/'policies']:
    if not p.exists(): errors.append(f"missing: {p.relative_to(ROOT)}")
try:
    raw_cfg=tomllib.loads((TEAM/'config.toml').read_text())
    cfg=raw_cfg['agents']
    if raw_cfg.get('model') != 'gpt-5.6-sol': errors.append('primary model must be gpt-5.6-sol')
    if raw_cfg.get('model_reasoning_effort') != 'low': errors.append('primary reasoning must be low')
    if cfg.get('enabled') is not True: errors.append('agents.enabled must be true')
    if not isinstance(cfg.get('max_concurrent_threads_per_session'), int): errors.append('max_concurrent_threads_per_session must be int')
    if cfg.get('default_subagent_model') != 'gpt-5.6-luna': errors.append('default subagent model must be gpt-5.6-luna')
    if cfg.get('default_subagent_reasoning_effort') != 'max': errors.append('default subagent reasoning must be max')
except Exception as e: errors.append(f'invalid config.toml: {e}')
required={'name','description','developer_instructions','model','model_reasoning_effort','sandbox_mode'}
names=set()
sol_agents={'product-manager','solution-architect','execution-planner','reviewer','security-reviewer'}
for p in sorted((TEAM/'agents').glob('*.toml')):
    try: d=tomllib.loads(p.read_text())
    except Exception as e: errors.append(f'invalid TOML {p.name}: {e}'); continue
    miss=required-d.keys()
    if miss: errors.append(f'{p.name}: missing {sorted(miss)}')
    n=d.get('name')
    if n in names: errors.append(f'duplicate agent name: {n}')
    names.add(n)
    expected_profile=('gpt-5.6-sol','low') if n in sol_agents else ('gpt-5.6-luna','max')
    actual_profile=(d.get('model'), d.get('model_reasoning_effort'))
    if actual_profile != expected_profile:
        errors.append(f'{p.name}: expected model profile {expected_profile}, got {actual_profile}')
expected={'product-manager','solution-architect','code-mapper','docs-researcher','ui-designer','execution-planner','frontend-developer','backend-developer','database-engineer','fullstack-developer','test-automator','browser-qa','reviewer','security-reviewer','debugger','deployment-engineer'}
if expected-names: errors.append(f'missing core agents: {sorted(expected-names)}')
if errors:
    print('Product team validation FAILED:')
    for e in errors: print('-',e)
    raise SystemExit(1)
print(f'Product team validation passed: {len(names)} agents')
