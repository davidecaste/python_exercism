(import (rnrs))

(define (digits n)
  (if (< n 10)
      (list n)
      (append (digits (quotient n 10))
              (list (remainder n 10)))))

(define (armstrong-number? n)
  (let* ((d (digits n))
         (len (length d)))
    (= (apply +
              (map (lambda (x) (expt x len)) d))
       n)))
