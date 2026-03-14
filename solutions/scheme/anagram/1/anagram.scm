(import (rnrs))

(define (toLowerCase string)
  (list->string
    (list-sort char<?
       (string->list (string-downcase string)))))

(define (anagram? target word)
  (and  (not (string-ci=? target word))
        (string=? 
            (toLowerCase target)
            (toLowerCase word))))

(define (anagram target words)
  (filter (lambda (w) (anagram? target w)) words))