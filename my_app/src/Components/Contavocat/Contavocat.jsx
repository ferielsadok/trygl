import React from 'react';
import './Contavocat.css';

const Contavocat = (props) => {
  return (
    <div className='avocat'>
      <div className='image'>
        <img src={props.image} alt='' />
      </div>
      <div className='info-container'>
        <p>
          {props.name}
          {props.prenom}
        </p>
        <p>{props.specialité}</p>
      </div>
    </div>
  );
};

export default Contavocat;
