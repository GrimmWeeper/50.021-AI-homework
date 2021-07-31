(define (domain logistic)

(:predicates 
    (location ?l) (truck ?t) (package ?p) 
    (at-location-truck ?a) (at-location-package ?p ?l) 
    (truck-free ?t) (truck-loaded-package ?t ?p)
)

(:action move-truck
    :parameters (?from ?to)
    :precondition (and (location ?from) (location ?to) (at-location-truck ?from))
    :effect (and (at-location-truck ?to) (not (at-location-truck ?from)))
)

(:action load-package
    :parameters (?p ?l ?t)
    :precondition (and (package ?p) (location ?l) (truck ?t) (at-location-truck ?l) (at-location-package ?p ?l) (truck-free ?t))
    :effect (and (truck-loaded-package ?t ?p) (not (at-location-package ?p ?l)) (not (truck-free ?t)))
)

(:action unload-package
    :parameters (?p ?l ?t)
    :precondition (and (package ?p) (location ?l) (truck ?t) (truck-loaded-package ?t ?p) (at-location-truck ?l))
    :effect (and (at-location-package ?p ?l) (truck-free ?t) (not (truck-loaded-package ?t ?p)))
)

)

