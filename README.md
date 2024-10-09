# Humus.py
## (A python client for) a composting database.

Simple python client for [Humus](https://github.com/timcowlishaw/humus), the forgetful database.

### Installation:

```bash
pip install humus.py # Not pip install humus, that's someone else's project that ironically does the complete opposite
```

### Usage:

First, make sure the [Humus server](https://github.com/timcowlishaw/humus) is running somewhere you can access it.

Then you can create a client object:


```python
import humus

# Create a client.
# Looks for HUMUS_PROTOCOL, HUMUS_HOST and HUMUS_PORT environment variables,
# or by default connects to humus on http://localhost:3030

client = humus.Client()

# Otherwise you can provide protocol, host and port as arguments:
client = humus.Client(host="somehost", port=1234, protocol="https")
```

Once you have your client, you can start storing and retrieving objects:

```python
# Put (any json-serializable) dict at a path:
client.insert("path/to/the_object", { "hello": "world"})

# Get objects at a path:
client.get("path/to/the_object")
# => [{ "hello": "world"}]
```

Further information on the humus, its data model, and our innovative and forward-thinking **strong guarantee of transience™** can be found in [the main humus repository](https://github.com/timcowlishaw/humus).


