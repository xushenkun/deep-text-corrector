
find "./dataset" -name '*.xml' -print0 | sort -z | -exec cat {} \; | grep -E '<p>' | awk '{$0=tolower($0);gsub(/<\/p>/,"\n");gsub(/<c>[^<]*<\/c>/,"");gsub(/([\.\?\(\)\[\]!,"])/," & ");gsub(/<[^>]*>/," ");gsub(/\sm[rs]\s\./," mr.");gsub(/ {2,}/," ");gsub(/^ */,"");printf("%s", $0);}' > './fce_source.txt'
find "./dataset" -name '*.xml' -exec cat {} \; | grep -E '<p>' | awk '{$0=tolower($0);gsub(/<\/p>/,"\n");gsub(/<i>[^<]*<\/i>/,"");gsub(/([\.\?\(\)\[\]!,"])/," & ");gsub(/<[^>]*>/," ");gsub(/\sm[rs]\s\./," mr.");gsub(/ {2,}/," ");gsub(/^ */,"");printf("%s", $0);}' > './fce_target.txt'

paste -d "\n" fce_source.txt fce_target.txt > fce_all.txt

#wc -l fce_all.txt

split -l 25708 fce_all.txt fce_

#awk '{ print split($0,a), length(), NR, $0 | "sort -rn" }' fce_all.txt | head -n 1