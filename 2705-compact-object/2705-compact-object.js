var compactObject = function(obj) {
    if (Array.isArray(obj)) return obj.filter(Boolean).map(compactObject);
    if (typeof obj !== 'object' || !obj) return obj;
    return Object.fromEntries(
        Object.entries(obj).filter(([, v]) => Boolean(v)).map(([k, v]) => [k, compactObject(v)])
    );
};