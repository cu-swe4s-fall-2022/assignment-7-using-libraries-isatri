#!/bin/bash
test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

run run_plotter \
    python3 ./plotter.py
assert_exit_code 0
assert_no_stdout
assert_no_stderr

declare -a arr=(iris_boxplot.png \
                petal_width_v_length_scatter.png \
                multi_panel_figure.png)

for file in "${arr[@]}"
do
    if test -f "$file"; then
        echo "$file exists."
    fi
done
