program Program;
    var int1, int2, int3: integer;
        real1, real2, real3: real;
begin
    int1 := 1 + 2;
    int2 := int2 + int3;
    int3 := (int1 + 2) + 3;
    int1 := 5;
    int2 := -5;

    real1 := 1 + 1;
    real2 := 1.2 + 2;
    real3 := 2 + 1.2;
    real1 := 1.1 + 1.2;
    real2 := (int1 + int2) * int3 - 2.5;
    real3 := real2
end.
