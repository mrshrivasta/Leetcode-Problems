var expect = function(val) {
    return {
        toBe: (v) => { if (val !== v) throw new Error("Not Equal"); return true; },
        notToBe: (v) => { if (val === v) throw new Error("Equal"); return true; }
    };
};