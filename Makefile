
.PHONY: all clean test install

OBJDIR=./build
TARGET=$(OBJDIR)/dist.alfredworkflow

all: $(TARGET)

$(TARGET): test $(OBJDIR)/icon.png $(OBJDIR)/info.plist
	zip -j -D $@ $?

$(OBJDIR)/icon.png: icon.svg
	@[ -d $(OBJDIR) ] || mkdir -p $(OBJDIR)
	convert -background None icon.svg $@

$(OBJDIR)/info.plist: query.py info.plist make-info.plist.py
	@[ -d $(OBJDIR) ] || mkdir -p $(OBJDIR)
	python make-info.plist.py

clean:
	rm -f *.pyc $(OBJDIR)/*

test:
	python -m unittest test_query

install: all
	open $(TARGET)
