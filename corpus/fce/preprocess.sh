
find "./dataset" -name '*.xml' -print0 | sort -z | xargs -0 cat | grep -E '<p>' | awk '{$0=tolower($0);gsub(/<\/p>/,"\n");gsub(/[.?()[\]!,"]/," & ");$0=gensub(/\sm(r|s|rs)\s\./," m\\1.","g");$0=gensub(/([0-9]) \. ([0-9])/,"\\1.\\2", "g");gsub(/p \. m \./, "p.m.");gsub(/u \. s \. a/, "u.s.a");gsub(/f \. c \. e/, "f.c.e");gsub(/b \. h \./, "b.h.");gsub(/a \. m \./, "a.m.");gsub(/p \. m \./, "p.m.");gsub(/m \. s \./, "m.s.");gsub(/e \. g \./, "e.g.");gsub(/p \. s \./, "p.s.");gsub(/a \. s \./, "a.s.");gsub(/t \. v \./, "t.v.");gsub(/o \. k/, "o.k");gsub(/\.\s\.\s\./,"...");gsub(/\.\s\./,".");gsub(/!\s!/,"!");source=gensub(/<c>[^<]*<\/c>/,"","g",$0);target=gensub(/<i>[^<]*<\/i>/,"","g",$0);gsub(/<[^>]*>/," ",source);gsub(/ {2,}/," ",source);gsub(/ *$/,"",source);slen=split(source,srcs," [.?!] ");gsub(/^ */,"",source);gsub(/<[^>]*>/," ",target);gsub(/ {2,}/," ",target);gsub(/ *$/,"",target);tlen=split(target,tgts," [.?!] ");for(i=1;i<=slen;i++){src=gensub(/^ */,"","g",srcs[i]);tgt=gensub(/^ */,"","g",tgts[i]);if(src!="\n"&&tgt!="\n")printf("src: %s\ndst: %s\n",src,tgt);}}' | tr -s '\n' > './fce_all.txt'

wc -l fce_all.txt

split -l 55514 fce_all.txt fce_

wc -l fce_ab

split -l 6940 fce_ab fce_test_val