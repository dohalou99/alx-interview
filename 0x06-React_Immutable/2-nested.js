import { fromJS } from 'immutable';

export default fucntion accessImmutableObject(Myobject, array) {
    const mappedObj = fromJS(Myobject);

    return mappedObj.getIn(array, undefined);
}
