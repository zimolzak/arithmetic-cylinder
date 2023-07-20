multi_word_configs.txt: letter_cylinder.py fourletter.txt
	python $< | sort -nr | uniq > $@

fourletter.txt: make_fourletter.py
	python $< > $@
