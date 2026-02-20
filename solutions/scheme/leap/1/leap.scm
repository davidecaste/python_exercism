(import (rnrs))

(define (leap-year? year)
    (or (= (remainder year 400) 0)
        (and (= (remainder year 4) 0)
           (not (= (remainder year 100) 0))
        )
    )
)

