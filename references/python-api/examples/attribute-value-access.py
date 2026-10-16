def radius_attribute(curves):
    radii = curves.attributes["radius"]
    return radii


def create_point_attribute(curves):
    ### Add a new attribute labeled `my_attribute_name` of type `float` on the point domain of the geometry.
    my_attribute = curves.attributes.new("my_attribute_name", 'FLOAT', 'POINT')
    return my_attribute


def remove_drawing_attribute(drawing):
    attribute = drawing.attributes["some_attribute"]
    drawing.attributes.remove(attribute)


def read_radii(curves):
    attributes = curves.attributes
    import numpy as np

    ### Get the radius attribute.
    radii = curves.attributes["radius"]
    ### Print the radius of the first point.
    print(radii.data[0].value)
    ### Output: 0.005

    ### Get the total number of points.
    num_points = attributes.domain_size('POINT')
    ### Create an empty buffer to read all the radii into.
    radii_data = np.zeros(num_points, dtype=np.float32)
    ### Read all the radii of the curves into `radii_data` at once.
    radii.data.foreach_get('value', radii_data)
    ### Print all the radii.
    print(radii_data)
    ### Output: [0.1, 0.2, 0.3, 0.4, ... ]
    return radii_data


def write_radii(curves):
    attributes = curves.attributes
    import numpy as np

    radii = curves.attributes["radius"]
    ### Write a radius with a value of 0.5 to the first point.
    radii.data[0].value = 0.5
    print(radii.data[0].value)
    ### Output: 0.5

    num_points = attributes.domain_size('POINT')
    ### Generate random radii with values between 0.001 and 0.05 using numpy.
    new_radii = np.random.uniform(0.001, 0.05, num_points)
    ### Write the new radii to the radius attribute.
    radii.data.foreach_set('value', new_radii)


def read_positions(curves):
    import numpy as np
    attributes = curves.attributes
    num_points = attributes.domain_size('POINT')
    positions = curves.attributes['position']
    ### Here, we're using a numpy array with shape (num_points, 3) so that each
    ### element is a 3d vector.
    positions_data = np.zeros((num_points, 3), dtype=np.float32)
    ### The `np.ravel` function will pass the `positions_data` as a flat array
    ### without changing the original shape.
    positions.data.foreach_get('vector', np.ravel(positions_data))
    print(positions_data)
    ### Output: [[0.1, 0.2, 0.3], [0.4, 0.5, 0.6], ...]
    return positions_data
