class EventEmitter {
    constructor() {
        this.events = new Map();
    }

    subscribe(eventName, callback) {
        if (!this.events.has(eventName)) this.events.set(eventName, []);
        this.events.get(eventName).push(callback);
        return {
            unsubscribe: () => {
                const cbs = this.events.get(eventName);
                cbs.splice(cbs.indexOf(callback), 1);
            }
        };
    }

    emit(eventName, args = []) {
        return (this.events.get(eventName) ?? []).map(cb => cb(...args));
    }
}