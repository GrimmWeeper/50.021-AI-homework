(define (problem logistic-delivery-simple) (:domain logistic)
(:objects 
    changi tampines bedok
    package1
    truck
)

(:init
    (location changi) (location tampines) (location bedok)
    (package package1)
    (truck truck)
    (at-location-truck tampines)
    (at-location-package package1 bedok)
    (truck-free truck)
)

(:goal (and (at-location-package package1 changi))
)

)
