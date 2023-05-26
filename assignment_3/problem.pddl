

(define (problem tpp-problem)
  (:domain tpp-domain)
  (:objects
    p1 p2 p3 - product
    m1 m2 m3 - market
    start-market - market
  )
  
  (:init
    (at-market start-market)
    (at-product p1 m1)
    (at-product p2 m2)
    (at-product p3 m3)
  )
  
  (:goal (forall (?p - product) (purchased ?p)))
)