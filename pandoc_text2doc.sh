pandoc --bibliography=refs.bib -o ${outfile}.docx -t docx ${infile}.tex --citeproc
