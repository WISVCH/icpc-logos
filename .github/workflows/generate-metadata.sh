#!/usr/bin/env bash
pwd
cd out/contest-package
jq "[.[] | {\"organization_id\": .id, \"name\": .formal_name, \"id\":1, \"group_ids\": [\"3\"], \"external_id\": .id, \"display_name\": .formal_name}] | to_entries | map( (.value.id = \"\(1+.key)\" ) | .value)" organizations.json > teams.json
cat > contest.yaml <<<"id:                            1
name:                          demo
title:                         demo
short-name:                    demo
start-time:                    2024-10-21T00:00:00.000Z
duration:                      5:00:00
scoreboard_freeze_duration:    1:00:00
scoreboard_type:               pass-fail
penalty_time:                  20
"
cat > groups.json <<<"[{\"id\":\"3\",\"icpc_id\":\"3\",\"name\":\"Contestants\"}]"
cd ../..
