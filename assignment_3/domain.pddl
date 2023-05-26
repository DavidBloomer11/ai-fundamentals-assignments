(define (domain tpp-domain)
  (:requirements :strips :typing)
  (:types market product)
  (:predicates
    (at-market ?m - market)
    (at-product ?p - product ?m - market)
    (purchased ?p - product)
  )
  
  (:action move
    :parameters (?from - market ?to - market)
    :precondition (at-market ?from)
    :effect (and (not (at-market ?from)) (at-market ?to))
  )
  
  (:action buy
    :parameters (?p - product ?m - market)
    :precondition (and (at-market ?m) (at-product ?p ?m))
    :effect (and (purchased ?p) (not (at-product ?p ?m)))
  )
)

