(import (rnrs))

(define (single x)
    (cond
        ((char=? x #\G) #\C)
        ((char=? x #\C) #\G)
        ((char=? x #\T) #\A)
        ((char=? x #\A) #\U)))

(define (dna->rna dna)
    (list->string 
     (map single (string->list dna))))


