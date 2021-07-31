(define (problem logistic-delivery-hard) (:domain logistic)
(:objects 
    changi tampines bedok
    package1 package2
    truck
)

(:init
    (location changi) (location tampines) (location bedok)
    (package package1)
    (package package2)
    (truck truck)
    (at-location-truck tampines)
    (at-location-package package1 bedok)
    (at-location-package package2 changi)
    (truck-free truck)
)

(:goal (and (at-location-package package1 changi) (at-location-package package2 bedok))
)

)
