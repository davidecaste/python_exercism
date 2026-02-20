(import (rnrs))

(define (square n)
  (assert (<= 1 n 64))
      (ash 1 (- n 1)))    ; ash è shift aritmetico -> ash(x, n) aggiunge n zeri alla rappresentazione binaria di x

(define total
    (- (ash 1 64) 1)) ; uso formula serie geometrica