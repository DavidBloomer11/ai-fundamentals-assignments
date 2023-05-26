  (:action move
    :parameters (start-market m3)
    :precondition
      (at-market start-market)
    :effect
      (and
        (not
          (at-market start-market)
        )
        (at-market m3)
      )
  )
  
    (:action move
    :parameters (start-market m3)
    :precondition
      (at-market start-market)
    :effect
      (and
        (not
          (at-market start-market)
        )
        (at-market m3)
      )
  )

  (:action move
    :parameters (m3 m2)
    :precondition
      (at-market m3)
    :effect
      (and
        (not
          (at-market m3)
        )
        (at-market m2)
      )
  )

    (:action buy
    :parameters (p2 m2)
    :precondition
      (and
        (at-market m2)
        (at-product p2 m2)
      )
    :effect
      (and
        (purchased p2)
        (not
          (at-product p2 m2)
        )
      )
  )

    (:action move
    :parameters (m2 m1)
    :precondition
      (at-market m2)
    :effect
      (and
        (not
          (at-market m2)
        )
        (at-market m1)
      )
  )


  (:action buy
    :parameters (p1 m1)
    :precondition
      (and
        (at-market m1)
        (at-product p1 m1)
      )
    :effect
      (and
        (purchased p1)
        (not
          (at-product p1 m1)
        )
      )
  )