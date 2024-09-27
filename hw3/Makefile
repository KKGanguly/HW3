# Default is show help; e.g.
#
#    make 
#
# prints the help text.
SHELL     := bash
MAKEFLAGS += --warn-undefined-variables
.SILENT:

Top=$(shell git rev-parse --show-toplevel)
Data ?= $(Top)/ezr_24Aug14/data/optimize
dirs ?= config hpo misc process
Tmp  ?= $(HOME)/tmp
Act  ?= randvsezr
threshold ?= 6 
Data_dir ?= data
less_dir ?= $(Data_dir)/less_than_$(threshold)
greater_dir ?= $(Data_dir)/greater_than_or_equals_$(threshold)
subdirs ?= $(addprefix $(Data)/, $(dirs))
CSV_Files := $(shell find $(subdirs) -name "*.csv")
Exp_dir ?= greater_than_or_equals_$(threshold)
exp_files=$(shell find $(Data_dir)/$(Exp_dir) -name "*.csv")
exp_directory=$(shell basename $(Exp_dir))
divide:
	mkdir -p $(less_dir) $(greater_dir); \
	echo "Classifying CSV files..."; \
	
	for file in $(CSV_Files); do \
		column_count=$$(head -n 1 $$file | sed 's/[^,]//g' | wc -c); \
		if [ $$column_count -lt $(threshold) ]; then \
			cp $$file $(less_dir); \
			echo "$$file has $$column_count columns, copied to $(less_dir)"; \
		else \
			cp $$file $(greater_dir); \
			echo "$$file has $$column_count columns, copied to $(greater_dir)"; \
		fi; \
	done
Out=output
act: ## experiment: mqs
	echo "mkdir -p $(Out)/$(Act)/$(exp_directory)"
	echo "rm -f $(Out)/$(Act)/$(exp_directory)/*"
	for file in $(exp_files); do \
		outfile=$$(basename "$$file"); \
		echo "python3 hw3.py -t $$file -e $$Act  | tee $(Out)/$(Act)/$(exp_directory)/$$outfile & "; \
	done 