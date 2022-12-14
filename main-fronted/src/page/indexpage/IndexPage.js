import React from 'react'
import LeftSide from "../../components/common/leftSide/LeftSide";
import RightSide from '../../components/common/rightSide/RightSide';
import TextArea from "../../components/common/textArea/TextArea"
import NavView from '../../components/SignViews/NavView';

function IndexPage() {
  return (
    <div>
      <NavView/>
      <div className="row">
        <div className="col-1">
          <LeftSide />
        </div>
        <div className="col-8">
          <TextArea />
        </div>
        <div className="col-3">
            <RightSide />
        </div>
      </div>
    </div>
  );
}

export default IndexPage