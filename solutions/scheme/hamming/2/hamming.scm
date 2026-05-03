(import (rnrs))

(define (hamming-distance strand-a strand-b)
    (if (not (= (string-length strand-a)
                (string-length strand-b)))
        (error "string of different length")
        (fold-left + 0
              (map (lambda (v1 v2)
                     (if (char=? v1 v2)
                         0
                         1
                         ))
                   (string->list strand-a)
                   (string->list strand-b)))))

