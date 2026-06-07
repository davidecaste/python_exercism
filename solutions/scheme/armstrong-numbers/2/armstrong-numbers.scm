(import (rnrs))

(define (armstrong-number? n)
  (let* ((digits (map (lambda (c) (- (char->integer c) 48))
                      (string->list (number->string n))))
         (len (length digits))
         (sum (apply +
                     (map (lambda (d) (expt d len))
                          digits))))
    (= sum n)))