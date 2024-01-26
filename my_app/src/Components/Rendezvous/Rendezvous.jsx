import React from 'react';
import './Rendezvous.css';
import rendez from '../../Assets/rendez-vous';

const Rendezvous = () => {
  return (
    <div className='everything-all'>
      <h1>Mes Rendez-Vous</h1>
      <div className='Rendez-passe-container'>
        <p>Rendez-vous passés</p>
        <div className='p-tags'>
          <p>Date</p>
          {rendez.map((rendez, i) => {
            {
              /*d agui a feriel avocat nni ernouyas s pour faire le link */
            }
            return (
              <AvocatfavUse
                key={i}
                id={avocat.id}
                name={avocat.name}
                specialité={avocat.specialité}
                image={avocat.cover}
              />
            );
          })}
          <p>Heure</p>
          <p>Avocat</p>
          <p>Option</p>
        </div>
      </div>
      <div className='Rendez-venir-container'>
        <p>Rendez-vous a venir</p>
        <div className='p-tags'>
          <p>Date</p>
          <p>Heure</p>
          <p>Avocat</p>
          <p>Option</p>
        </div>
      </div>
    </div>
  );
};

export default Rendezvous;
