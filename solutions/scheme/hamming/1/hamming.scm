(import (rnrs))

(define (hamming-distance strand-a strand-b)
    (define (count-iter pos cnt)
        (if (= pos (string-length strand-a))
            cnt
            (count-iter (+ pos 1)
                        (+ cnt
                            (if (char=? (string-ref strand-a pos)
                                        (string-ref strand-b pos))
                                0
                                1)))))  
  
  (if (not (= (string-length strand-a)
              (string-length strand-b)))
    (error "string of different length")
    (count-iter 0 0)))

