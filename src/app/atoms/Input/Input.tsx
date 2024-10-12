import React from 'react';
import styles from './Input.module.css';

interface InputProps extends React.InputHTMLAttributes<HTMLInputElement> {
    label: string;
    placeholder?: string; 
}

const Input: React.FC<InputProps> = ({ label, placeholder, ...props }) => {
    return (
        <div className={styles.inputContainer}>
            <label className={styles.label}>{label}</label>
            <input className={styles.input} placeholder={placeholder} {...props} />
        </div>
    );
};

export default Input;
