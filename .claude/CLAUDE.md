# CodeGraph First Workflow

## IMPORTANT

Always use CodeGraph MCP tools FIRST before:

* grep
* glob
* repository-wide scanning
* recursive file reading

## Preferred Workflow

1. Use CodeGraph context tools
2. Use dependency graph analysis
3. Use callers/callees analysis
4. Use impact analysis
5. Read only minimal required files

## Avoid

* Full repository exploration
* Reading unrelated files
* Broad grep searches
* Repeated recursive scans

## Goals

* Minimize token usage
* Minimize unnecessary reads
* Use structural graph understanding first
* Apply minimal code changes

## Preferred Tools

* codegraph_context
* codegraph_search
* codegraph_callers
* codegraph_callees
* codegraph_impact

## Editing Rules

Before editing:

* analyze dependencies
* analyze impact radius
* trace execution flow

After editing:

* validate affected callers
* ensure minimal modifications

## Mandatory Tool Priority

Tool priority order:

codegraph_context
codegraph_search
codegraph_callers
codegraph_callees
codegraph_impact
read_file
grep
glob

Never start with repository-wide scanning unless explicitly requested.
