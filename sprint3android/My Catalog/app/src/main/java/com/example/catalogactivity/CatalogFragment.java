package com.example.catalogactivity;

import android.content.Intent;
import android.os.Bundle;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;
import androidx.fragment.app.Fragment;

import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;

public class CatalogFragment extends Fragment {

    public CatalogFragment() {

    }

    public static CatalogFragment newInstance(String param1, String param2) {
        CatalogFragment fragment = new CatalogFragment();

        return fragment;
    }

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        if (getArguments()!= null) {

        }

    }
    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
        // Inflar el layout del fragment
        View view = inflater.inflate(R.layout.fragment_catalog, container, false);
        // Configuración del botón para navegar al detalle
        Button navegar = view.findViewById(R.id.button_navegar);
        navegar.setOnClickListener(v -> {
            // Navegar a DetailActivity
            Intent intent = new Intent(getActivity(), DetailActivity.class);
            startActivity(intent);
        });
        return view;
    }
}