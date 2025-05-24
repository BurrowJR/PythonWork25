# Alyssa was asked to write an implementation of a rolling buffer.
# You can add and remove elements from a rolling buffer.
# However, once the buffer becomes full, any new elements will displace
# the oldest elements in the buffer.

# She wrote two implementations of the code for adding elements to the buffer:
def add_to_rolling_buffer1(buffer, max_buffer_size, new_element):
    # append mutates the original list
    buffer.append(new_element)
    if len(buffer) > max_buffer_size:
        buffer.pop(0)
    return buffer

def add_to_rolling_buffer2(buffer, max_buffer_size, new_element):
    # a new buffer list is created the original list is unchanged
    buffer = buffer + [new_element]
    if len(buffer) > max_buffer_size:
        buffer.pop(0)
    return buffer